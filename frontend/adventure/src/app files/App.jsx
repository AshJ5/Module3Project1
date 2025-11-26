import { useState } from 'react'
import './App.css'
import IntroPage from '../intropage/intropage'
import TitlePage from '../titlepage/titlepage'
import CharacterPage from '../characterpage/character'

function App() {
  const [showTitle, setShowTitle] = useState(false);
  const [showCharacter, setShowCharacter] = useState(false);

  return (
    <>
      {!showTitle ? (
        <IntroPage onAnimationComplete={() => setShowTitle(true)} />
      ) : !showCharacter ? (
        <TitlePage onStart={() => setShowCharacter(true)} />
      ) : (
        <CharacterPage />
      )}
    </>
  )
}

export default App
