
const FetchData = async (url, params={}) => {
    const call = await fetch(url, params);
    const data = await call.json();
    return data;
};

const FetchData2 = async (url, params={}) => {
  const call = await fetch(url, params);
  const data = await call.blob();
  console.log((data));
  return data;
};

$('input#fileContainer').on('change', function () {
    // console.log(this);

    let reader = new FileReader();
    reader.onload = function (e) {
        // console.log(reader.result + '->' + typeof reader.result)
        let thisImage = reader.result;
        localStorage.setItem("imgData", thisImage);
    };
    reader.readAsDataURL(this.files[0]);
});


const upload = (file) => {
    body = JSON.stringify({
        "image": file
    })
    FetchData2('http://localhost:5000/give_image', {method: 'POST', headers: {
        'Content-Type': 'application/json'
      }, body: body}).then((data) => {
  // console.log("success: ", data); 
  localStorage.setItem("vidData", data);
  // document.getElementById("video").innerHTML 
  // let vidCtr = $('<video/>').prop('src', vidData);
  // $('div#video').append(vidCtr);
  const src = window.URL.createObjectURL(data)
  const el = document.getElementById('video')
  el.src = src
  el.play()

}).catch((e) =>{
  console.log(e);
}

);
  };

  $('input#show').click(function () {
    let dataImage = localStorage.getItem('imgData');
    // console.log(dataImage);
    upload(dataImage);
    // let imgCtr = $('<img/>').prop('src', dataImage);
    // $('div#imgContainer').append(imgCtr);
});
