# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Camera.py'],
    pathex=[],
    binaries=[],
    datas=[('icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Camera',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='Camera.app',
    icon='icon.ico',
    bundle_identifier='com.yourname.camera',
    info_plist={
        'NSCameraUsageDescription': 'This app needs access to the camera to take photos.',
        'CFBundleDisplayName': 'Camera App',
        'CFBundleShortVersionString': '1.0.0',
    },
)