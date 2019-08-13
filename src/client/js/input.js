import { updateDirection, updateLeftClick } from './networking';

var mousedownID = -1;  //Global ID of mouse down interval

function mousedown(event) {
  if(mousedownID==-1)  //Prevent multimple loops!
     mousedownID = setInterval(whilemousedown, 20 /*execute every 20ms*/);
}

function mouseup(event) {
   if(mousedownID!=-1) {  //Only stop if exists
     clearInterval(mousedownID);
     mousedownID=-1;
   }
}

function whilemousedown() {
  updateLeftClick()
}

function onMouseInput(e) {
  handleInput(e.clientX, e.clientY);
}

function onTouchInput(e) {
  const touch = e.touches[0];
  handleInput(touch.clientX, touch.clientY);
}

function handleInput(x, y) {
  const dir = Math.atan2(x - window.innerWidth / 2, window.innerHeight / 2 - y);
  updateDirection(dir);
}

export function startCapturingInput() {
  window.addEventListener('mousemove', onMouseInput);
  window.addEventListener("mousedown", mousedown);
  window.addEventListener("mouseup", mouseup);
  //Also clear the interval when user leaves the window with mouse
  window.addEventListener("mouseout", mouseup);
  window.addEventListener('touchstart', onTouchInput);
  window.addEventListener('touchmove', onTouchInput);
}

export function stopCapturingInput() {
  window.removeEventListener('mousemove', onMouseInput);
  window.removeEventListener("mousedown", mousedown);
  window.removeEventListener("mouseup", mouseup);
  window.removeEventListener("mouseout", mouseup);
  window.removeEventListener('touchstart', onTouchInput);
  window.removeEventListener('touchmove', onTouchInput);
}
