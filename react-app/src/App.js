import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
// import NavBar from './components/NavBar/index';
import ErrorPage from './components/ErrorPage';
import ProtectedRoute from './components/auth/ProtectedRoute';
import { authenticate } from './store/session';
import HomePage from './components/HomePage.js';
import NavBar from './components/NavBar';
import Player from './components/Player';
// import MainSidebar from './components/MainSidebar';
import Library from './components/Library'
import YourLibraryPage from './components/YourLibraryPage';
import { PathProvider } from './context/PathContext';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();
  const user = useSelector(({ session }) => session.user);

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <PathProvider>
        {user && <NavBar />}
        <Switch>
          <Route path='/login' exact={true}>
            <LoginForm />
          </Route>
          <Route path='/sign-up' exact={true}>
            <SignUpForm />
          </Route>
          <ProtectedRoute path='/' exact={true} >
            <HomePage />
          </ProtectedRoute>
          <ProtectedRoute path={`/library`}>
            <Library />
            {/* <MainSidebar /> */}
          </ProtectedRoute>
          <ProtectedRoute path='/library' exact={true} >
            <YourLibraryPage />
          </ProtectedRoute>
          <Route path="*">
            <ErrorPage />
          </Route>
        </Switch>
        {user && (
          <>
            {/* <MainSidebar /> */}
            <Player />
          </>
        )}
      </PathProvider>
    </BrowserRouter>
  );
}

export default App;
