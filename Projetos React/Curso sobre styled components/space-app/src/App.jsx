import styled from "styled-components"
import GlobalStyles from "./components/styles/GlobalStyles";
import Cabecalho from "./components/Cabecalho";
import MainSearchInput from "./components/MainSearchInput";
import SideBar from "./components/SideBar";

function App() {
  const FundoGradiente = styled.div`
    background: var(--Gradiente-fundo, linear-gradient(175deg, #041833 4.16%, #04244F 48%, #154580 96.76%));
    width: 100%;
    min-height: 100vh;
  `;

  return (
    <FundoGradiente>
      <GlobalStyles />
      <Cabecalho>
        <MainSearchInput />
      </Cabecalho>
      <SideBar/>
    </FundoGradiente>
  )
}

export default App
