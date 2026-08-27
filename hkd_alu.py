# -*- coding: utf-8 -*-
# HKD OBFUSCATE v4 - portable source payload, no marshal/code-object dependency.
# Protection is import-time only; protected functions have no per-call wrapper.
def _hkd_v4_bootstrap(_g):
    import binascii as _hb
    import hashlib as _hh
    import struct as _hs
    import zlib as _hz

    _b = (
        _hb.unhexlify('8c410163faea967c647849fb5cf293a7276aad9fea868006c9dbade3da23f1e61f4c3e87741c5356c3a1b216694197473b4e59563fce616631823c9d8c946dc09fe835585216e89f9ccd99845a1c4122ae8d551b1c9369cf28518f33794991747cd40f4d93ce45985bb9289665b5960f92e1d6883fd34a54c6d41c9a5ef43ee4'),
        _hb.unhexlify('aa727d6a768adfc77f331561847b958c483425248c2bf21f693518389ff6fb494dac14984478253f30de2a720af6eea2bf0b0ba1e5139357173021647e2d6fd1aa8c21f21d79dc5167b61f18edc6a46ef37ffb7a33ad4adad5dd929f7390109ba4debf6bfaac885eb0dc95fdce640069baf6ce38955a153fe05e11a0f63ae323'),
        _hb.unhexlify('b9c77d2d4441e6ab897a9fd396ca889e7d8f9db14ebcd4fb20d31891fb7b62458aec3ebcff7ac7d55263ea308c0ef7b56ff99271da61ed7c751064184df7cc36823e91748b1e34d31e18eeb7fd34a1ee2de274ecf71507f006cf7f74133aaf928a984c15b3973fc62d082d06c48e116e6758c89a649be7b42f6f61cdd5e942ed'),
        _hb.unhexlify('9bc556595940d2ead3447dde9c70ab7b884b3b1ef5b3367906648e4e1e088d8c9d71135bc1496800072c04a8aaaed4df98539cb727684232d9eb2219b8d5142c8025021787b24c7eea6a763546c96d9601ada996f5288ff5bad4888023b861b159093ea4fefee936b6b4fc3b574aa0ed7833606754f959291a3bbe6d748d561d'),
        _hb.unhexlify('45db5d35c54491ee3df680ea19b4ea97393f7f8c0767a20fd02e44ba075a9163df8bab00ac1e9cbd04ce2c4be863ca02498c4be6727e49b7d48554e8b67e1d3dea75c101b78100449d2cefbdc21ca5daca9ea2228a3b39d98b14676a07d731fb51362147cdf4af1d44db1eed3b9e78bccfee9cfe15b5514bcc8743e77fc14691'),
        _hb.unhexlify('91321754ef950c163805ec91216d568534f8536f8c6ba8485bef37ac30a8da88b2f28f6927b94a4144acdbb0f98edbdbf54b8cd2a9e5c43ee7fa5b5b4a5d2ef6c50143bf501888d1b407d05ab7211e145a5e4b5a16054ab582b565efcf8ab83c0157318fdea319761e409470bfc8c493486f61f3810b3426dbd498745bb05be7'),
        _hb.unhexlify('eedf0f924f945d5758e7c8861ca6262b9baeddbad5ef14249942350d145fa5a5b0d57ac4c7001ccfb13c2031c42a7a7d8bd969e203b303007e64f0a3ce0e90fe4b5bc9ad62d23443275312915b33c3b2df03e6704e771fd30d0b161f1f1ad2191cff8a59e7fc9f595cc2955d120865d23ffaea0e4c5f1f01887a2c949c91c75f'),
        _hb.unhexlify('22e35143823cba6aedaa712fabc794cfd35c237f34fcad724d5a1136b1494df2a9bb5e151a6b86a95496896ed3e1639c1df5c8fe42044afe2377b1e5803470bf7d21012354a3429d1ed52e994c62972bae14201c75cf1d44de86b366be3d277847eaf4d309d8794742bff062805058fa9655f489fb132685d3d34df3e01481c8'),
        _hb.unhexlify('2bbc0f1d6cb6a64619301e231792dbd4b934e25a6f7535dc9de35b7d14a9402f1c38a8942311f9f6e6310aeda83cd1006a138617154985343553714c473f5a139b8cec568a2a486cb9bea2292ff66736b4bdf2e3350cf8ea8f731e1d55144c474e04f2ee3af5b41ec1a3912bdee54232e0c27d57a618d0a859936acd0c22fb66'),
        _hb.unhexlify('377c7bfa73592ef54041e199b4f8af670ec903aa1458c57bd7ca759b3815830dea322cfce5d3f5db589183e9c56709f391d1528a6a0923326289ab35f97ef270b7c3d5d3bdac47577d8ba4f62e5cfee086674209e847197c8d0ace866ef02dcf7e7c99d6d922f3f34e9362847aa666f0ffe0777a29a32bfb3c19963ae0f72f1d'),
        _hb.unhexlify('bbeb4184600cf770e5707ff67e0cf7d7d3b2b4b867342a6515212b44797440fa4746051c480253a15601c8bc2b4f9749cb2ab0629c144cd211c3862465a55729232b7ca0c3733cb349db8772864d8251160ababd28242a1dfecc62daaaaa9f9c405da302b550a4dd39b303f03b406854badf554c0056ea0a2d5e182e16ec3058'),
        _hb.unhexlify('4febf0f53bf74df8fcf37eccc27e5de719b4245c8e8e44dc4c0a0129f4'),
    )
    _inv = (1, 6, 3, 5, 9, 4, 8, 2, 7, 10, 0, 11)
    _leaves = (
        _hb.unhexlify('2a82be2bb0bc0dfb180ea9f23b75ad5d3705e84163b12a2eae3b77ace13a3b8a'),
        _hb.unhexlify('8f9c5873685c6a0b2fe334641f581100f8031b53caaa5210d53276866fa0d61d'),
        _hb.unhexlify('c74e8b7904c5eef29d69f070826cc0f46f98fe99668a0fda4f2ca836addbc7f9'),
        _hb.unhexlify('8cc258acf9b283b411dc01ecd304337c5cb443c8ae0022a6b30de92a6149fbd6'),
        _hb.unhexlify('0753971cd747f325cda3cefccbd9919b4f841797fc2466467819b5945d8da21a'),
        _hb.unhexlify('afe9530b38e989afbfbece2e09d26b7a01cc37c4938cf2c5d650a9fb2997ac11'),
        _hb.unhexlify('eefc459d4277851d4641d33cca5302aff086ed0b4803d2cc7e7c7bc37acabb8c'),
        _hb.unhexlify('c5d943007f6779f1d4409e9ce0e14ec57b3366e565b85dccd8aa0af0cc8a13ce'),
        _hb.unhexlify('e6d872e359ee0d022985048b771b651c582b3ab93e531fa93b72c5f91966957a'),
        _hb.unhexlify('d665a3310383235bd37f5c405ec3b6b45825b0e07e384a119decda76a65b8fdb'),
        _hb.unhexlify('c8b70cb9e4ce25fdc82d045d12e5ee5725c365821b5fbfb8332d0c6d145c17c7'),
        _hb.unhexlify('ad42b5c60a306c4fbad22228f81bddafa97313edae65314b5a416ee8d869797d'),
    )
    _root = _hb.unhexlify('bba95cedcb5b21d0bf90601ce8ba3f8f321efbf939890aa71705ce45276017d0')
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
