import { updateMoveDirection, updateLookDirection, updateLeftClick } from './networking';

var mousedownID = -1;  //Global ID of mouse down interval
var updateDirectionTimer = -1
var leftdownID = false;
var updownID = false;
var rightdownID = false;
var bottomdownID = false;
var direction = -1

function findMoveDirection() {
  if (updownID && rightdownID){
    direction = 0.25 * Math.PI
  }
  else if (rightdownID && bottomdownID){
    direction = 0.75 * Math.PI
  }
  else if (bottomdownID && leftdownID){
    direction = 1.25 * Math.PI
  }
  else if (leftdownID && updownID){
    direction = 1.75 * Math.PI
  }
  else if (updownID)
  {
    direction = 0
  }
  else if (rightdownID)
  {
    direction = 0.5 * Math.PI
  }
  else if (bottomdownID)
  {
    direction = Math.PI
  }
  else if (leftdownID)
  {
    direction = 1.5 * Math.PI
  }
  else {
    direction = -1
  }
  return direction
}

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

function intervalKeyDown(varIntervalID, direction){
  console.info("IntervalKeyDown", varIntervalID, direction)
  if(varIntervalID==-1){
    varIntervalID = setInterval(updateDirection(direction), 20);
  }
}

function intervalKeyUp(varIntervalID){
  console.info("IntervalKeyUp", varIntervalID)
  if(varIntervalID==-1){
    clearInterval(varIntervalID);
    varIntervalID=-1;
  }
}

function whilemousedown() {
  updateLeftClick()
}

function onMouseInput(e) {
  handleLookDirection(e.clientX, e.clientY);
}

function handleLookDirection(x, y) {
  const dir = Math.atan2(x - window.innerWidth / 2, window.innerHeight / 2 - y);
  updateLookDirection(dir);
}

function updatingMoveDirection(){
  updateMoveDirection(findMoveDirection())
}

function handleKeyDown(e) {
  // z
  if (event.keyCode == 90 | event.keyCode == 122){
    console.info("handleKeyDown GO UP")
    updownID = true
  }
  // d
  else if (event.keyCode == 68 | event.keyCode == 100){
    rightdownID = true
  }
  // s
  else if (event.keyCode == 83 | event.keyCode == 115){
    bottomdownID = true
  }
  // q
  else if (event.keyCode == 81 | event.keyCode == 113){
    leftdownID = true
  }
}


function handleKeyUp(e) {
  // z
  if (event.keyCode == 90 | event.keyCode == 122){
    console.info("handleKeyDown STOP UP")
    updownID = false
  }
  // d
  else if (event.keyCode == 68 | event.keyCode == 100){
    rightdownID = false
  }
  // s
  else if (event.keyCode == 83 | event.keyCode == 115){
    bottomdownID = false
  }
  // q
  else if (event.keyCode == 81 | event.keyCode == 113){
    leftdownID = false
  }
}


export function startCapturingInput() {
  window.addEventListener('mousemove', onMouseInput);
  window.addEventListener("mousedown", mousedown);
  window.addEventListener("mouseup", mouseup);
  //Also clear the interval when user leaves the window with mouse
  window.addEventListener("mouseout", mouseup);
  // Handle zqsd keyboard
  window.addEventListener('keydown', handleKeyDown);
  window.addEventListener('keyup', handleKeyUp);
  updateDirectionTimer = setInterval(updatingMoveDirection, 20);
}

export function stopCapturingInput() {
  window.removeEventListener('mousemove', onMouseInput);
  window.removeEventListener("mousedown", mousedown);

  window.removeEventListener("mouseup", mouseup);
  window.removeEventListener("mouseout", mouseup);

  window.removeEventListener('keydown', handleKeyDown);
  window.removeEventListener('keyup', handleKeyUp);
  updateDirectionTimer = -1
}
