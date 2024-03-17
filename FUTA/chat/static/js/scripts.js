var videos = document.getElementsByClassName("postvid");
var currentlyPlayingId;

function videoControl(videoId) {
  var video = document.getElementById("video" + videoId); // Check if video is currently playing

  if (video.paused) {
    // If video is paused, play it
    video.play();
    currentlyPlayingId = videoId;
  } else {
    // If video is playing, pause it and revert time to 0m 0s
    video.pause();
    video.currentTime = 0;
  }
}

// Function to pause all videos and revert their time to 0m 0s
function pauseAllVideos() {
  for (var i = 0; i < videos.length; i++) {
    videos[i].pause();
    videos[i].currentTime = 0;
  }
}

// Event listener for each video's reactions
for (var i = 0; i < videos.length; i++) {
  var video = document.getElementById("video" + (i + 1));
  var reactionIcon = document.querySelector(
    ".reactions img:nth-child(" + (i + 1) + ")"
  ); // Event listener for video play

  reactionIcon.addEventListener("click", function () {
    // Pause all videos and revert their time to 0m 0s
    pauseAllVideos(); // Play the clicked video

    videoControl(this.parentElement.id.charAt(7));
  });
}
