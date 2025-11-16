// ------------------------------
// Developer: Jayani (US-002)
// Task: Integrate Upload UI with Backend API (/predict)
// ------------------------------

document.getElementById('uploadBtn').addEventListener('click', async () => {
  const input = document.getElementById('imageInput');
  const result = document.getElementById('result');

  // Step 1: Check if file selected
  if (!input.files || input.files.length === 0) {
    alert('⚠️ Please choose an image first.');
    return;
  }

  const file = input.files[0];

  // Step 2: Validate file type
  if (!['image/png', 'image/jpeg'].includes(file.type)) {
    alert('❌ Only PNG or JPG images are allowed.');
    return;
  }

  // Step 3: Show upload progress message
  result.innerText = '⏳ Uploading image and requesting prediction...';

  // Step 4: Send file to backend API
  try {
    const formData = new FormData();
    formData.append('file', file);

    // Call Flask backend API (Scrum Master built /predict endpoint)
    const response = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      // ✅ Fixed this line – added backticks for proper template literal
      throw new Error(`Server returned ${response.status}`);
    }

    const data = await response.json();

    // Step 5: Display result from backend stub
    if (data.label) {
      result.innerHTML = `
        ✅ <b>Prediction:</b> ${data.label}<br>
        🎯 <b>Confidence:</b> ${(data.confidence * 100).toFixed(1)}%
      `;
    } else {
      result.innerText = '⚠️ No label received from backend.';
    }

  } catch (error) {
  console.error('Error:', error);
  // This is the new validation block
  if (error.message.includes('Failed to fetch')) {
    result.innerText = '❌ Error: Backend server is not running. Please start Flask.';
  } else {
    result.innerText = `❌ Error: ${error.message}`;
  }
}

  // Step 6: Optional debug message (for testing)
  console.log("✅ Upload & backend integration complete (US-002)");
});
