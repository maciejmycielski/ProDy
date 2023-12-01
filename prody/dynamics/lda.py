# -*- coding: utf-8 -*-
"""This module defines a class for linear discriminant analysis (LDA) calculations."""

import time

import numpy as np

from prody import LOGGER
from prody.atomic import Atomic
from prody.ensemble import Ensemble
from prody.utilities import isListLike

from .nma import NMA

__all__ = ['LDA']


class LDA(NMA):

    """A class for linear discriminant analysis (LDA) of conformational
    ensembles. See examples in :ref:`pca`."""

    def __init__(self, name='Unknown'):
        NMA.__init__(self, name)

    def calcModes(self, coordsets, labels, n_modes=None, **kwargs):
        """Calculate linear discriminant analysis modes between classes.  
        This method uses :class:`sklearn.discriminant_analysis.LinearDiscriminantAnalysis`
        on coordsets with class labels.

        *coordsets* argument may be one of the following:

        * :class:`.Atomic`
        * :class:`.Ensemble`
        * :class:`.TrajBase`
        * :class:`numpy.ndarray` with shape ``(n_csets, n_atoms, 3)``

        :arg labels: a set of labels for discriminating classes
        :type labels: :class:`~numpy.ndarray`

        :arg n_modes: number of non-zero eigenvalues/vectors to calculate,
            default is **None**,
            if **None** or ``'all'`` is given, all modes will be calculated
        :type n_modes: int
        """
        try:
            from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
        except ImportError:
            raise ImportError("Please install sklearn to use LDA")

        start = time.time()
        self._clear()
        if str(n_modes).lower() == 'all':
            n_modes = None

        if isinstance(coordsets, np.ndarray):
            if (coordsets.ndim != 3 or coordsets.shape[2] != 3 or
                    coordsets.dtype not in (np.float32, float)):
                raise ValueError('coordsets is not a valid coordinate array')
        elif isinstance(coordsets, Atomic):
            self._coordsets = coordsets._getCoordsets()
        elif isinstance(coordsets, Ensemble):
            self._coordsets = coordsets._getCoordsets()

        nconfs = self._coordsets.shape[0]
        if not isListLike(labels):
            raise TypeError('labels must be either a list or a numpy.ndarray, not {0}'
                            .format(type(labels)))
        if not isinstance(labels, np.ndarray):
            labels = np.array(labels)
        if labels.ndim != 1 or len(labels) != nconfs:
            raise ValueError('labels should have same number as conformers')
        
        self._n_atoms = self._coordsets.shape[1]
        
        self._coordsets = self._coordsets.reshape(nconfs, -1)
        self._labels = labels

        n_components = kwargs.pop('n_components', n_modes)
        self._lda = LinearDiscriminantAnalysis(n_components=n_components, **kwargs)
        self._projection = self._lda.fit(self._coordsets, self._labels)

        values = self._lda.explained_variance_ratio_
        self._eigvals = values
        self._n_modes = len(self._eigvals)
        self._vars = values
        self._n_modes = len(self._eigvals)

        vecs = self._lda.scalings_
        self._array = np.array([vecs[:,i]/(vecs[:,i]**2).sum()**0.5 for i in range(self._n_modes)]).T

        if self._n_modes > 1:
            LOGGER.debug('{0} modes were calculated in {1:.2f}s.'
                     .format(self._n_modes, time.time()-start))
        else:
            LOGGER.debug('{0} mode was calculated in {1:.2f}s.'
                     .format(self._n_modes, time.time()-start))

    def addEigenpair(self, eigenvector, eigenvalue=None):
        """Add eigen *vector* and eigen *value* pair(s) to the instance.
        If eigen *value* is omitted, it will be set to 1.  Eigenvalues
        are set as variances."""

        NMA.addEigenpair(self, eigenvector, eigenvalue)
        self._vars = self._eigvals

    def setEigens(self, vectors, values=None):
        """Set eigen *vectors* and eigen *values*.  If eigen *values* are
        omitted, they will be set to 1.  Eigenvalues are set as variances."""

        self._clear()
        NMA.setEigens(self, vectors, values)
        self._vars = self._eigvals
