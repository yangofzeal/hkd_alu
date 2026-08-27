# -*- coding: utf-8 -*-
# HKD OBFUSCATE v4 - portable source payload, no marshal/code-object dependency.
# Protection is import-time only; protected functions have no per-call wrapper.
def _hkd_v4_bootstrap(_g):
    import binascii as _hb
    import hashlib as _hh
    import struct as _hs
    import zlib as _hz

    _b = (
        _hb.unhexlify('b5a8fbe0e548952ca0ab81994dee272bbeaf43fdbb7b39118e77670c4d14c062d638307e515802224d8c76efe2e34783acb14e892646461f43d77167b42c7da708cb3666db3878dda940f049c805a536d3e0bcb3b7cafb07666e4e5d5e291ed5f67c3f08daf16ad1675b30b7a6ad2036d60a38350b65279479adeff1865a1f4a'),
        _hb.unhexlify('966fd92dbd9bef9f61d7cb6d1bec636605fc807c42b46fccd44bd756c88dd0bcea47da58a266e1aace20f4a79f841b702ee15b7458add1fcf5c2184de2809d8584887651d2195f175eb5ac5e32c836cbb35c7914822d0b85b06fc561b486f2e3ceef345b974ba56f7fe2cc2f1314cd6d63a5c58b1348a0124e29b3b67a56b991'),
        _hb.unhexlify('6baa40b6e53793357ddb3ab33504b4c0d24587171c64963fb56df8487dcd6d9b728bad33bd6a9bb6588160c6e62d12d425407e1155240c39555d808258cd7292eb635eb746af013a995733b68d861f00ee8d34f2fe5926ef0326bc61fd8e3a1b93f38553574780440aff1fbc2fbc1b39f2f00de267bfdb0a52063bfb02f07554'),
        _hb.unhexlify('1de253e052ff87b8d970f0fbde66edda116e7e04e93bb50d84a27f3eaceb34e384bf060de93b90373804cd5efcfa14a0aec4f50c7a92f604609b9176b430c4b25a4f68d789ee83079d2a69bac2add7aec7c5e0c94d9a520a8be5430d947e1a91ac49f23698c45b77708c00afefd29d81118e906ec1fdde0f0a82da1383aeb2ec'),
        _hb.unhexlify('8005fb4b592503e63068a62287caf47f4f6e346df60f2a8995c98194f7f5752079ed1792a2fae1e36a69798b65a6f06fd6a241385f2b36f9dfece548f8edf7e69168ae4ebb9895ce7bc65eb758d8e8743d23b72d66ff847e53de68c38c51ef38663d5d25d93c93397ae2f52727865be768c5653e30b8cfa53449fb57d52b4eef'),
        _hb.unhexlify('9c59b7fbd155ff0799779d68950adb'),
        _hb.unhexlify('df1a495eb2f7e71ca246fc76a9b3a472c8f95c31a4108becdc3acc4447ab97ed2e30fa05e6b8edbc754fac5603ecf76da42a82ee09b6f9f56db518f76270933f4add489625b8213e402d8b55a1b706295f2966d801c30410cf3d69a34b55f38c9dc8e657b89d1b09db744cae7305dc98bd69b18cc492c01b2b05e5b60e268108'),
        _hb.unhexlify('aa727d6a768adfc77f331561847b958c883dc5208c39f21f69d559389ff6fb494dbad139e52498ccd3e9da7c60d515a45e19e5ab019056d1886c116940ebda28b88c38c64af82be8328846541b83fc5e53b6c656f5dee020713d3b7f79a41298b47f90810fb4c35e5f00175f711667cbb4b35cf03c23f9c9f622bf836ec628fa'),
        _hb.unhexlify('594bcf50bfe772c00934dae5e81656b48df9a30a6d80fc55621f176e28247b45612e6f54b4821a49a7c7f2d677c1dba76fe87e3ad97a28c971d4c9f90efc5de3dde6949bb8e97ba0eeeb511aa35ffa6b09f22e9310d91fd16ceffec4f900e98fd2b5ff7b036699e129c572e220d92c04931fd14b41b73ac1e5f60db0607d4f24'),
        _hb.unhexlify('2dd16c5ffaefc2b29eb99ebd272bffd1ddf41397c2011c605dd99e4083bcce5f5ffd9b58f6fd374df24769f685ec00959504d5d92109b9e2c2932d1371a84723004b37988a38bfea799d44cf18b48e8e11e4d7c44f5598ba3c6405cac651f642ed3e3a79fe20ad532f685df24c35e775e574780b6077d3ead797037fa790b9cf'),
        _hb.unhexlify('3c559773bdd1ee41ea839f3b9d0b043531577ffaa85fe366dbebe3576956e56553af661ae84622fed72788b4d009c18dcb1b33b691cc28b386f56a1738b0fc9c23950910be4e8d671b370d0f4b7baeba964b4f9d8a9614162fd870f452bfbac6a0dfdfa2650531d7168e07434ab95d2e998421e2f5cd3072d01913b8a05eb64d'),
        _hb.unhexlify('ced2dfbcc7ee16fd9b1632befe6662ee102ee7326acef5900cba93f92328eb790c912c2e81563118e77ba7dc211069e61820dbd19344a031c6aa56d641cc07da482dacb09e9149fa259c8c9f939e0d4513adb5066115cc2ddf8121e7e0e4926a3cdc9d42ed906d134ce844dff8efa9896dcaf0b3dae67b384a0ef78c2aba9eb7'),
    )
    _inv = (7, 6, 10, 9, 0, 2, 3, 1, 8, 4, 11, 5)
    _leaves = (
        _hb.unhexlify('c61cf6f4d71e103033d6d983aadd817d9fd7b389bb177b1642d9216dc394242a'),
        _hb.unhexlify('abad733426dd08b1bc1597977debd2aa5851e624e37148ef4236f601ac4703e6'),
        _hb.unhexlify('ecd7799f49ee25f810b1901a84d90230be361f5e156c945bf80afa6b0a8a3926'),
        _hb.unhexlify('6316c1225a3e75ca6e105d7e4f7162c3ec01f932c2629b9b777d1b69194e3843'),
        _hb.unhexlify('2d48d56161e9ffd5be8974f439547369f9106b6f69c34a266dba28aeee6b41aa'),
        _hb.unhexlify('2c5b930d5db29429db5c761a3dbcdf46fb88b0bcc8177c9cba0c635213cae2fd'),
        _hb.unhexlify('a01a7f85c101c32efff5cfc40327d98efe08263ba812d1a06d60d68686c165bc'),
        _hb.unhexlify('92000877358e5d4579f1daf3e178aa949e2ce57da4c2d089b710fd130fff5567'),
        _hb.unhexlify('55c0886e4d8804393247b02260b859c2935e9bfad968a3387522351fc5978705'),
        _hb.unhexlify('56bb8e6b97a31051cfa239a23c9e0b37f1f280f562cd340a269740fb41676fd4'),
        _hb.unhexlify('16a8c016830fa22881137858f415869dc66127104ac5af43722374a4855eb777'),
        _hb.unhexlify('0609bf4488aa03bf84f442543887c9e46564a60d034861aec042eaab0dc190d5'),
    )
    _root = _hb.unhexlify('f40f2dffb45cf20e695e80f59376c4a7419afb545abf8d55944164cba6981fc7')
    _share1 = _hb.unhexlify('55eda5f163d89abc0fa9ee2f50360fb8a1798cbdee89b7724aa601d666ef165c')
    _share2 = _hb.unhexlify('9f79c9c5af812421529d38fa0edc11dc26853438e917cd18eb1ba098b56c4e3b')

    def _u32(_n):
        return _hs.pack('>I', _n)


    def _xor(_a, _c):
        _o = bytearray(len(_a))
        _i = 0
        while _i < len(_a):
            _o[_i] = _a[_i] ^ _c[_i]
            _i += 1
        return bytes(_o)

    def _ks(_key, _index, _length):
        _o = bytearray()
        _counter = 0
        _seed = _key + _u32(_index)
        while len(_o) < _length:
            _o.extend(_hh.sha256(_seed + _u32(_counter)).digest())
            _counter += 1
        return bytes(_o[:_length])

    def _merkle(_values):
        if not _values:
            return _hh.sha256(b'').digest()
        _level = list(_values)
        while len(_level) > 1:
            if len(_level) & 1:
                _level.append(_level[-1])
            _next = []
            _i = 0
            while _i < len(_level):
                _next.append(_hh.sha256(_level[_i] + _level[_i + 1]).digest())
                _i += 2
            _level = _next
        return _level[0]

    _key = _xor(_share1, _share2)
    _parts = []
    _verify = []
    _i = 0
    while _i < len(_inv):
        _masked = _b[_inv[_i]]
        _raw = _xor(_masked, _ks(_key, _i, len(_masked)))
        _parts.append(_raw)
        _verify.append(_hh.sha256(_u32(_i) + _raw).digest())
        _i += 1

    if tuple(_verify) != _leaves or _merkle(_verify) != _root:
        raise ImportError('HKD protected payload integrity verification failed')

    try:
        _source = _hz.decompress(b''.join(_parts)).decode('utf-8')
    except Exception as _exc:
        raise ImportError('HKD protected payload reconstruction failed: %s' % (_exc,))

    _filename = _g.get('__file__') or '<HKD-obfuscated>'
    _code = compile(_source, _filename, 'exec', 0, True, 0)

    # Discard the plaintext string before running user code.  CPython may reclaim
    # it immediately; no plaintext source is retained as a module global.
    del _source

    # Return the compiled payload.  Keep exec out of this function: older
    # CPython parsers reject an exec statement in a function that also contains
    # nested functions/free variables.  Execution happens at module scope below.
    return _code

_hkd_v4_code = _hkd_v4_bootstrap(globals())
del _hkd_v4_bootstrap

# Exact module semantics: execute in the real module globals.
exec(_hkd_v4_code, globals(), globals())
del _hkd_v4_code
