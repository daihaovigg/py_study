# -*- mode: python -*-
a = Analysis(['app.py'],
             pathex=['/home/dai/py_study/web/exe'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='app',
          debug=False,
          strip=None,
          upx=True,
          console=True )
