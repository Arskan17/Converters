document.getElementById('resizeForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const fileInput = document.getElementById('image');
    const width = parseInt(document.getElementById('width').value);
    const height = parseInt(document.getElementById('height').value);
    const file = fileInput.files[0];
    
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = new Image();
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = width;
                canvas.height = height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0, width, height);
                
                const resizedImageURL = canvas.toDataURL('image/jpeg');
                const downloadLink = document.createElement('a');
                downloadLink.href = resizedImageURL;
                downloadLink.download = 'resized_image.jpg';
                downloadLink.textContent = 'Download Resized Image';
                downloadLink.className = 'btn btn-primary';
                
                const resultDiv = document.getElementById('result');
                resultDiv.innerHTML = '';
                resultDiv.appendChild(downloadLink);
            };
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});
