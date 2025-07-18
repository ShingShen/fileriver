# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['fileriver.py'],
    pathex=[],
    binaries=[],
    datas=[('filetraffic', 'filetraffic'), ('cli.py', '.'), ('http_server.py', '.'), ('http_server_files', 'http_server_files')],
    hiddenimports=['netifaces', 'pyftpdlib', 'pyftpdlib.authorizers', 'pyftpdlib.handlers', 'pyftpdlib.servers', 'tftpy', 'flask'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='fileriver',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
