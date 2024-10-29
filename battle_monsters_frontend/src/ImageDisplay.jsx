import React, { useEffect, useState } from 'react';

function ImageDisplay({ jsonFilename }) {
  const [imageData, setImageData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchImageData = async () => {
      try {
        const response = await fetch(`http://localhost:5000/send-image/${jsonFilename}`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setImageData(data.img);
      } catch (error) {
        setError(error.message);
      }
    };

    fetchImageData();
  }, [jsonFilename]);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!imageData) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{jsonFilename}</h1>
      <img src={`data:image/jpg;base64,${imageData}`} alt="Card" />
    </div>
  );
}

export default ImageDisplay;