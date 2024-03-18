var currentVideo = null;
function videoControl(video) {
  var video = document.getElementById(video);
  if (currentVideo && currentVideo !== video) {
    currentVideo.pause();
    currentVideo.currentTime = 0;
  }
  if (video.paused) {
    video.play();
    currentVideo = video;
  } else {
    video.pause();
    currentVideo = null;
  }
}
