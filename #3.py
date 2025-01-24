import numpy
# numpy.sign(x, /, out=None, *, where=True, casting='same_kind', order='K',
  #     dtype=None, subok=True[, signature, extobj])
  
y = (163,165,162,189,161,171,158,151,169,
      182,163,139,172,165,148,166,172,163,187,173)

print(numpy.sign(y, out=None, where=True, casting='same_kind', order='K',
    dtype=None, subok=True))
