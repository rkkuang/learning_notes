Python 多核并行计算
https://zhuanlan.zhihu.com/p/24311810

当计算时间比较长的时候，我们可能想要加上一个进度条，这个时候 i 系列的好处就体现出来了。另外，有一个小技巧，就是输出 \r 可以使得光标回到行首而不换行，这样就可以制作简易的进度条了。

cnt = 0
for _ in pool.imap_unordered(f, xs):
    sys.stdout.write('done %d/%d\r' % (cnt, len(xs)))
        cnt += 1
