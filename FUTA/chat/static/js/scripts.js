function videoControl(videoId) {
    var videos = document.querySelectorAll('.postvid'); // Get all video elements
  
    // Find the targeted video
    var video = document.getElementById("video" + videoId);
  
    // Toggle playback based on the video's current state
    video.paused ? video.play() : video.pause();
  }
  
  window.onload = function () {
    // Bind event handlers to all reaction icons
    var videos = document.querySelectorAll('.reaction-icon');
  
    videos.forEach(function (video, index) {
      video.addEventListener('click', function () {
        var videoId = index + 1; // Assuming video IDs start from 1 (adjust if needed)
        videoControl(videoId);
      });
    });
  };
  