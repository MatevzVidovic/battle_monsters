import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import CounterButton from './CounterButton.jsx'
import './index.css'

import ImageDisplay from './ImageDisplay.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    <CounterButton />
    <div className="text-center mt-4">
    </div>
    <ImageDisplay jsonFilename="Nasa_patched.json" />
  </StrictMode>,
)
