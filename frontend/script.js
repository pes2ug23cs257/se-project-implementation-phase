document.getElementById('uploadBtn').addEventListener('click', () => {
  const input = document.getElementById('imageInput');
  if (!input.files || input.files.length === 0) {
    alert('Choose an image first');
    return;
  }
  const file = input.files[0];
  if (!['image/png','image/jpeg'].includes(file.type)) {
    alert('Only PNG/JPG allowed');
    return;
  }
  document.getElementById('result').innerText = 'Ready to send to API (mock).';
});
