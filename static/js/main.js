$(document).ready(function () {
  $(".addfiles").on("click", function () {
    $("#img").click();
    return false;
  });

//  $("#divya").hide();

//  $(".batti-green3").hide();

  var head = document.getElementById("headinf");
  var para = document.getElementById("paragraf");

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                console.log('Image loaded')
            }
            reader.readAsDataURL(input.files[0]);
        }

        var form_data = new FormData($('#upload-file')[0]);
        console.log(form_data)

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                head.innerHTML = data[0]
                para.innerHTML = data[1]
                console.log('Result: ' + data);
            },
        });
    }

    $("#img").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

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
