import styled from "styled-components";

// eslint-disable-next-line react/prop-types
const Cabecalho = ({children}) => {
  const StyledHeader = styled.header`
    padding:  30px 0;
    display: flex;
    justify-content: space-between; 
    padding: 10px 30px;
  `;
  return (
    <StyledHeader>
      <img src="/imagens/logo.png" alt="" style={{width: '211.418px', height: '65px'}}/>
      {children}
    </StyledHeader>
  )
}

export default Cabecalho;