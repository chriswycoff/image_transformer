
const FetchData = async (url, params={}) => {
    const call = await fetch(url, params);
    const data = await call.json();
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
    FetchData('http://localhost:5000/give_image', {method: 'POST', headers: {
        'Content-Type': 'application/json'
      }, body: body}).then((data) => {
  console.log("success: ", data); 
}).catch((e) =>{
  console.log(e);
}

);
  };

  $('input#show').click(function () {
    let dataImage = localStorage.getItem('imgData');
    console.log(dataImage);
    upload(dataImage);
    // let imgCtr = $('<img/>').prop('src', dataImage);
    // $('div#imgContainer').append(imgCtr);
});
