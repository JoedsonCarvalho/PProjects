import styled from "styled-components";

const StyledInput = styled.input`
width: 380px;
height: 30px;
border-radius: 10px;
background: transparent;
border: 2px solid var(--Degrad-com-rosa, #C98CF1);
padding: 12px 16px;
background-image: url("icon/search.png");
background-repeat: no-repeat;
background-size: 20px 20px;
background-position: 98% 50%;
&::placeholder{
  color: #D9D9D9;
}
`;

const MainSearchInput = () => {
  return (<>
    <StyledInput
      // style={{border: 'none'}}
      placeholder="Search..."
    />
  </>)
}

export default MainSearchInput;