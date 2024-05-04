import React, { useState, useEffect } from "react";
import styled from "styled-components";

const Button = styled.button`
  background-color: #004d40;
  color: white;
  padding: 5px 15px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  box-shadow: 0px 2px 2px lightgray;
  margin: 0px 2px;
  transition: ease background-color 250ms;
  &:hover {
    background-color: #009688;
  }
`;

function App() {
  return (
    <div>
      <Button>E</Button>
      <Button>F</Button>
      <Button>F#</Button>
      <Button>G</Button>
      <Button>G#</Button>
      <Button>A</Button>
      <Button>A#</Button>
      <Button>B</Button>
      <Button>C</Button>
      <Button>C#</Button>
      <Button>D</Button>
      <Button>D#</Button>
    </div>
  );
}

export default App;
