import styled from "styled-components";

const StyledUl = styled.ul`
color: white;
list-style: none;
li{
  margin-bottom: 8px;
}
`;

const StyledAnchor = styled.a`
display: flex;
font-size: 18px;
align-items: center;
&:visited{
  color: white;
}
&:link{
  color: white;
}
&{
  text-decoration: none;

}
&:hover{
  cursor: pointer;
}
`;

const StyledIconImg = styled.img`
width: 30px;
height: 30px;
`;

const SideBar = () => {
  return (
    <>
      <aside style={{width: '240px'}}>
        <nav>
          <StyledUl>
            <li><StyledAnchor href="#">
              <i style={{marginRight: '5px'}}><StyledIconImg src="icon/home-ativo.png" alt=""/></i> Inicio</StyledAnchor>
            </li>
            <li><StyledAnchor href="#">
              <i style={{marginRight: '5px'}}><StyledIconImg src="icon/mais-vistas-ativo.png" alt=""/></i> Mais Vistas</StyledAnchor>
            </li>
            <li><StyledAnchor href="#">
              <i style={{marginRight: '5px'}}><StyledIconImg src="icon/mais-curtidas-ativo.png" alt=""/></i> Mais Curtidas</StyledAnchor>
            </li>
            <li><StyledAnchor href="#">
              <i style={{marginRight: '5px'}}><StyledIconImg src="icon/novas-ativo.png" alt=""/></i> Novas</StyledAnchor>
            </li>
            <li><StyledAnchor href="#">
              <i style={{marginRight: '5px'}}><StyledIconImg src="icon/surpreenda-me-ativo.png" alt=""/></i> Surpreenda-Me</StyledAnchor>
            </li>
          </StyledUl>
        </nav>
      </aside>
    </>
  )
}

export default SideBar;