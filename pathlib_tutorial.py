from pathlib import Path

def demo1():
    path_1 = Path('/twtrubiks') / Path('hello')
    print(path_1) # PosixPath('/twtrubiks/hello')
    print(str(path_1))

    path_2 = Path('/twtrubiks') / 'hello' / 'world'
    print(path_2)

    path_3 = Path('/twtrubiks') / 'hello' / Path('world')
    print(path_3)

    path_4 = Path('/twtrubiks').joinpath('test1', 'test2/test3')
    print(path_4)

    path_5 = Path('/twtrubiks', 'test2', 'test3')
    print(path_5)

    print("絕對路徑:", path_5.absolute())

    print("比對路徑:")
    if Path('/twtrubiks') == Path('hello'):
        print("相同")
    else:
        print("不相同")

    print("命令列上 執行位置路徑:", Path(__file__))

    print("目前路徑:", Path.cwd())
    print("home 路徑:", Path.home())

    # 擁有者
    print("擁有者:", Path.cwd().owner())

def demo2():
    path = Path(Path.cwd(), 'myfile.txt')
    if path.exists():
        print('已存在')
    else:
        print('不存在, 建立檔案')
        path.touch()
        print('已經建立')
        print('是否存在:', path.exists())
        # path.unlink() # 刪除路徑檔案

def demo3():
    path = Path(Path.cwd(), 'myfile.txt')
    print("path.resolve():", path.resolve())
    print(path.name)
    print("檔名:", path.stem)
    print("副檔名:", path.suffix)
    print("is_file:", path.is_file())
    print("is_dir:", path.is_dir())
    print("is_symlink:", path.is_symlink())
    print("檔案大小:", path.stat())
    print("檔案大小:", path.stat().st_size) # bytes
    print("取出全部副檔名:", Path('test.tar.bz1').suffixes)

def demo4():
    # 簡單檔案讀寫
    path = Path(Path.cwd(), 'myfile.txt')
    print("讀檔:", path.read_text())

    path.write_text('Hello')
    print("讀檔:", path.read_text())

    with path.open('w') as f:
        f.write('Hello 123')
    print("讀檔:", path.read_text())

def demo5():
    # 走訪某資料夾內的所有檔案與資料夾
    my_path = Path.cwd()
    for f in Path(my_path).iterdir():
        print(f.name)

def demo6():
    print("查看上層目錄")
    path =  Path('/twtrubiks/a1/a2/a3/test.py')
    print(path.parent)
    print(path.parent.parent)

    print("查看全部上層目錄")
    for path in path.parents:
        print(path.parent)

def demo7():
    path = Path.cwd()
    data = list(Path(path).glob('*.py'))
    print("路徑下全部有 .py 結尾的檔案:", data)

def demo8():
    # https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser
    """
    Return a new path with expanded ~ and ~user constructs, as returned by os.path.expanduser().
    If a home directory cant be resolved, RuntimeError is raised.
    """
    p = Path('~/hello/test123')
    print(p.expanduser())

def demo9():
    # https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.with_suffix
    path = Path(Path.cwd(), 'test.json')
    print("with_suffix")
    print(path)
    print(path.with_suffix(''))
    print(path.with_suffix('.py'))
    print(path.with_suffix('.zip'))

    # https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.with_name
    path = Path.cwd()
    print("with_name")
    print(path)
    print(path.with_name('test.py'))
    print(path.with_name('a123.222'))

def demo10():
    path = Path.cwd()
    n_path = path / Path('p1/p2/p3/test.py')
    print("階層建立資料夾:")
    n_path.mkdir(parents=True)

if __name__ == "__main__":
    demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    # demo7()
    # demo8()
    # demo9()
    # demo10()

