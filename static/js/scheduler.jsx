function Hello() {
    return (
     
     <h1  style={{
        fontSize: "80px",
        alignItems: "center",
        marginLeft:"850px"
    }} >Welcome to Isma Melon!</h1>
     
    );
  }

  ReactDOM.render(<Hello/>, document.querySelector("#root"));


  function LoginButton(props) {

    return <button type="submit" 
    style={{
            backgroundColor: "white",
            fontSize: "25px",
            width: "250px",
            margin: "4px",
            alignItems: "center"}} >

            {props.message}

            </button>;
  }
  
  ReactDOM.render(<LoginButton message="Login" />, document.querySelector("#buttons-login"));
 