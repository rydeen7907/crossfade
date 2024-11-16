＝＝＝＝＝
＜ 参考 ＞
fourccを使って動画保存をする

＝＝＝＝＝

fourcc は、ビデオコーデックを指定するものであり、ビデオの品質に影響を与えます。 
fourcc を変更することで、圧縮率、ファイルサイズ、画質などを調整できます。

fourcc を設定する方法はいくつかあります。
- OpenCV 3.4.0 以前の方法：fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
- OpenCV 3.4.0 以降の方法：fourcc = cv2.VideoWriter_fourcc(*'MJPG')

1: 定数
# XVID コーデック (一般的なコーデック)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# MJPEG コーデック (画質が良いが、ファイルサイズが大きくなる傾向がある)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

# H264 コーデック (高圧縮率、画質が良い、ファイルサイズが小さい)
fourcc = cv2.VideoWriter_fourcc(*'X264')

# DIVX コーデック (一般的なコーデック)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

2: 文字列
# XVID コーデック
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

# MJPEG コーデック
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

# H264 コーデック
fourcc = cv2.VideoWriter_fourcc('H','2','6','4')

# DIVX コーデック
fourcc = cv2.VideoWriter_fourcc('D','I','V','X')

3: コーデックID
# XVID コーデック (コーデック ID は 0x00000021)
fourcc = cv2.VideoWriter_fourcc(0x00000021)

# MJPEG コーデック (コーデック ID は 0x00000056)
fourcc = cv2.VideoWriter_fourcc(0x00000056)

# H264 コーデック (コーデック ID は 0x00000022)
fourcc = cv2.VideoWriter_fourcc(0x00000022)

# DIVX コーデック (コーデック ID は 0x00000022)
fourcc = cv2.VideoWriter_fourcc(0x00000022)

これらのコーデック ID は、OpenCV のドキュメントで確認できます。

どの fourcc を選択するかは、使用するビデオプレーヤー、必要なビデオ品質、ファイルサイズなどの要因によって異なります。

・高画質と大きいファイルサイズ: MJPEG
・高圧縮率、画質が良い、小さいファイルサイズ: H264
・一般的なコーデック: XVID, DIVX

注意:
一部のコーデックは、特定のプラットフォームまたはビデオプレーヤーではサポートされていない可能性があります。
fourcc の変更は、ビデオの品質とファイルサイズに影響します。 最適な fourcc は、アプリケーションによって異なります。
この情報が fourcc の選択に役立つことを願っています。