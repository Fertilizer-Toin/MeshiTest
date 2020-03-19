githubの使い方ー！

コマンドプロンプトにいって任意のカレントディレクトリを作る。 

例) CD Desktop 

上の場合デスクトップを指定している 

次に 

git clone https://github.com/Fertilizer-Toin/MeshiTest.git 

このコマンドを打つ。 

するとカレントディレクトリに指定したファイルの中にMeshiTestというフォルダができる。  

そこをカレントディレクトリとする  

CD MeshiTest 

↑コレを打つ 

で、 

git pull origin master 

これうって 

中にファイルを入れたり、ファイルを編集したりして、その後 

git add 操作したファイル名 (変更したファイルを一発で全部ぶちこみたければgit add -A)

これをうって 
はげはげはげ

git commit -m "任意のコメント" (あとからみてなにしたかがわかるコメントをよろしく)

これうって 

git push origin master 

これうつ 

終わり。 

ProgateのGit講座をやってもいいかもしれない。