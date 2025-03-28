# STRIVE.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['D:\\PycharmProjects\\pythonProject\\app'],
    binaries=[],
    datas=[
        ('D:\\PycharmProjects\\pythonProject\\.venv\\Lib\\site-packages\\ultralytics\\cfg\\default.yaml', 'ultralytics/cfg'),
        ('D:\\PycharmProjects\\pythonProject\\app\\bg.jpg', '.'),
        ('D:\\PycharmProjects\\pythonProject\\app\\bg1.jpg', '.'),
        ('D:\\PycharmProjects\\pythonProject\\app\\login.png', '.'),  # Ensure this file exists
        ('D:\\PycharmProjects\\pythonProject\\app\\loginbg.jpg', '.'),
        ('D:\\PycharmProjects\\pythonProject\\app\\data.db', '.'),
        ('D:\\PycharmProjects\\pythonProject\\app\\strive.png', '.'),
        ('D:\\PycharmProjects\\pythonProject\\app\\best.pt', '.'),
        # Including an entire directory
        ('D:\\PycharmProjects\\pythonProject\\app\\images', 'images'),
        # Add other data files or directories as needed
    ],
    hiddenimports=[],
    hookspath=[],
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
    name='STRIVE',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='D:\\PycharmProjects\\pythonProject\\app\\strive.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='STRIVE',
)
