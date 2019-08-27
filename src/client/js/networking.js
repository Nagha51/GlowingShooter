import io from 'socket.io-client';
import { throttle } from 'throttle-debounce';
import { processGameUpdate } from './state';

const Constants = require('../shared/constants');

const socket = io.connect(`ws://${window.location.host}`);


const connectedPromise = new Promise(resolve => {
  socket.on('connect', () => {
    console.log('Connected to server!');
    resolve();
  });
});


export function processServerInfo(info) {
  console.log(info["message"])
}

export const connect = OnGameOver => (
  connectedPromise.then(() => {
    // Register callbacks
    socket.on(Constants.MSG_TYPES.INFO, processServerInfo);
    socket.on(Constants.MSG_TYPES.GAME_UPDATE, processGameUpdate);
    socket.on(Constants.MSG_TYPES.GAME_OVER, OnGameOver);
    socket.on('disconnect', () => {
      console.log('Disconnected from server.');
      OnGameOver()
      document.getElementById('disconnect-modal').classList.remove('hidden');
      document.getElementById('reconnect-button').onclick = () => {
        window.location.reload();
      };
    });
  })
);

export const play = username => {
  socket.emit(Constants.MSG_TYPES.JOIN_GAME, username);
};

export const updateMoveDirection = throttle(20, dir => {
  if (dir >= 0) {
    console.log("updateMoveDirection", dir)
    socket.emit(Constants.MSG_TYPES.MOVE, dir);
  }
  else {
    socket.emit(Constants.MSG_TYPES.MOVE, Constants.MSG_TYPES.STOP_MOVE);
  }
});

export const updateLookDirection = throttle(20, dir => {
  socket.emit(Constants.MSG_TYPES.LOOK, dir);
});

export const updateLeftClick = throttle(20, () => {
  socket.emit(Constants.MSG_TYPES.LEFT_CLICK)
});
