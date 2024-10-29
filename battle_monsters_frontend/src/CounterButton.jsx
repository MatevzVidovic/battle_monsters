import React, { useState } from 'react';

function CounterButton() {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <button
      onClick={handleClick}
      className="bg-blue-500 hover:bg-blue-700 rounded text-white font-bold px-4 py-2"
    >
      I have been clicked {count} times
    </button>
  );
}

export default CounterButton;