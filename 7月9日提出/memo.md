* ランタノイドは４f軌道以外Xeと同じ電子配置を持つ。(５s,５pは埋まっている)。
Tbの遷移は内側にあるf軌道間で起こるため結晶場の影響を受けにくい。
Euの遷移は最外殻の５dに遷移するため結晶場の影響を受けやすい。
なぜ４fより先に５s,５pが埋まるか？→そのほうが低エネルギー。というか４fがめっちゃ高エネルギー。
s＜p＜d＜fでfが出現しうるのは主量子数が４以上のとき。
内側なのに高エネルギーなんだ。。。

* 禁制-許容について
function execCopy(string) {
	// 空div 生成
	var tmp = document.createElement('div');
	// 選択用のタグ生成
	var pre = document.createElement('pre');

	// 親要素のCSSで user-select: none だとコピーできないので書き換える
	pre.style.webkitUserSelect = 'auto';
	pre.style.userSelect = 'auto';

	tmp.appendChild(pre).textContent = string;

	// 要素を画面外へ
	var s = tmp.style;
	s.position = 'fixed';
	s.right = '200%';

	// body に追加
	document.body.appendChild(tmp);
	// 要素を選択
	document.getSelection().selectAllChildren(tmp);

	// クリップボードにコピー
	var result = document.execCommand('copy');

	// 要素削除
	document.body.removeChild(tmp);
	alert(string);
	return result;
}

var note = prompt('記載事項');
var today = new Date().toLocaleDateString();
var url = location.host;
var memo = '日付:' + today + '\n' + '記載事項:' + note + '\n' + 'URL:' + url;
execCopy(memo);
function execCopy(string) {
	// 空div 生成
	var tmp = document.createElement('div');
	// 選択用のタグ生成
	var pre = document.createElement('pre');

	// 親要素のCSSで user-select: none だとコピーできないので書き換える
	pre.style.webkitUserSelect = 'auto';
	pre.style.userSelect = 'auto';

	tmp.appendChild(pre).textContent = string;

	// 要素を画面外へ
	var s = tmp.style;
	s.position = 'fixed';
	s.right = '200%';

	// body に追加
	document.body.appendChild(tmp);
	// 要素を選択
	document.getSelection().selectAllChildren(tmp);

	// クリップボードにコピー
	var result = document.execCommand('copy');

	// 要素削除
	document.body.removeChild(tmp);
	alert(string);
	return result;
}

var note = prompt('記載事項');
var today = new Date().toLocaleDateString();
var url = location.host;
var memo = '日付:' + today + '\n' + '記載事項:' + note + '\n' + 'URL:' + url;
execCopy(memo);
