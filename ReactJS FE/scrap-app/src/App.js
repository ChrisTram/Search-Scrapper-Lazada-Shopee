import './App.css';

import {Home} from './Home';
import {Products} from './Product';
import {Navigation} from './Navigation';

import {BrowserRouter, Routes, Route} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    <div className="container">
     <h3 className="m-3 d-flex justify-content-center">
       Scrap Shopee
     </h3>

     <Navigation/>
     <Routes>
       <Route path='/' element={<Home/>} exact/>
       <Route path='/products'  element={<Products/>}/>
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;