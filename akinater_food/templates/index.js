window.addEventListener("DOMContentLoaded", init);

function init() {
  const width = 960;
  const height = 540;

  // レンダラーを作成
  const renderer = new THREE.WebGLRenderer({
    canvas: document.querySelector("#myCanvas")
  });
 

  // シーンを作成
  const scene = new THREE.Scene();
　　
  // カメラを作成
  const camera = new THREE.PerspectiveCamera( 45,  width / height,
    1,10000
  );
  camera.position.set(0, 200, +1000);

  // 箱を作成
  const geometry = new THREE.PlaneGeometry(500, 500, 500);
  const material = new THREE.MeshStandardMaterial({color: 0x0000ff});
  const box = new THREE.Mesh(geometry, material);
  box.rotation.x = Math.PI / -2;
  scene.add(box);

  // 平行光源
  const light = new THREE.DirectionalLight(0xffffff);
  light.intensity = 2; // 光の強さを倍に
  light.position.set(1, 1, 1);
  // シーンに追加
  scene.add(light);

  // 初回実行
  tick();

  function tick() {
    requestAnimationFrame(tick);
    // レンダリング
    renderer.render(scene, camera);
  }
  onResize();
// リサイズイベント発生時に実行
window.addEventListener('resize', onResize);

function onResize() {
  // サイズを取得
  const width = window.innerWidth;
  const height = window.innerHeight;

  // レンダラーのサイズを調整する
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(width, height);

  // カメラのアスペクト比を正す
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
}
}
