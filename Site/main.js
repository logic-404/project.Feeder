$(document).ready(function () {
  $(".addfiles").on("click", function () {
    $("#img").click();
    return false;
  });

  $("#divya").hide();

  $(".batti-green3").hide();

  var head = document.getElementById("headinf");
  var para = document.getElementById("paragraf");

  const fileInput = document.querySelector("#img");
  fileInput.addEventListener("change", handleFileUpload);

  function handleFileUpload(event) {
    const file = event.target.files[0];
    const form_data = new FormData();
    form_data.append("img", file);

    // Send an AJAX request to the server to predict the uploaded image
    $.ajax({
      type: "POST",
      url: "/predict",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: true,
      success: function (data) {
        // Get and display the result
        console.log(" Result:  " + data);
      },
      error: function (xhr, textStatus, errorThrown) {
        console.log("Error:", textStatus);
      },
    });
  }

  //   function unhide() {
  //     $("#divya").show();
  //     setTimeout(function () {
  //       var a = $("input[type=file]").val();
  //       const b = a.split("\\");
  //       console.log(b[2]);
  //     }, 2000);
  //   }

  //   function loadTodo() {
  //     fetch("http://127.0.0.1:5000")
  //       .then((data) => {
  //         return data.json();
  //       })
  //       .then((jsondata) => {
  //         head.innerHTML = jsondata.dname;
  //         $("#image-to-hide").hide();
  //         para.innerHTML = jsondata.dabout;
  //       });
  //   }
});
