function videoControl(videoId) {
    var videos = document.querySelectorAll('.postvid'); // Get all video elements
  
    videos.forEach(function(video) {
      video.pause();
    });
  
    var video = document.getElementById("video" + videoId);
    video.play();
  }
  
  window.onload = function () {
    var videos = document.querySelectorAll('.reaction-icon');
  
    videos.forEach(function (video, index) {
      video.addEventListener('click', function () {
        var videoId = index + 1;
        videoControl(videoId);
      });
    });
  };
  