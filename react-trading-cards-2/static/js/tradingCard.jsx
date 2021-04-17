// var tradingCardData = [
//   {
//     name: 'Balloonicorn',
//     skill: 'video games',
//     imgUrl: '/static/img/balloonicorn.jpg'
//   },

//   {
//     name: 'Float',
//     skill: 'baking pretzels',
//     imgUrl: '/static/img/float.jpg'
//   },

//   {
//     name: 'Llambda',
//     skill: 'knitting scarves',
//     imgUrl: '/static/img/llambda.jpg'
//   }
// ];

function TradingCard(props) {
  return (
    <div className="card">
      <p>Name: {props.name}</p>
      <img src={props.imgUrl} />
      <p>Skill: {props.skill} </p>
    </div>
  );
}

// function TradingCardContainer() {
//   const [cards, updateCards] = React.useState([]);


//   React.useEffect(() => {
//     // stuff we want to happen during the components happy life
//     fetch('/cards.json')
//     .then((response) => response.json())
//     .then((data) => updateCards(data))
//   })

//   // const floatCard = {
//   //   name: 'Float',
//   //   skill: 'baking pretzels',
//   //   imgUrl: '/static/img/float.jpg'
//   // };

//   const tradingCards = [];

//   for (const currentCard of cards) {
//     tradingCards.push(
//       <TradingCard
//         key={currentCard.name}
//         name={currentCard.name}
//         skill={currentCard.skill}
//         imgUrl={currentCard.imgUrl}
//       />
//     );
//   }

//   return (
//     <div>{tradingCards}</div>
//   );

// }

function TradingCardContainer() {
  const [cards, updateCards] = React.useState([]);

  React.useEffect(() => {
    fetch("/cards.json")
      .then((response) => response.json())
      .then((data) => updateCards(data.cards));
  }, []);

  const tradingCards = [];

  // you can uncomment this console.log (line 27) to see the
  // value of the cards object what is it initially?
  // what about after the component re-renders?
  // if you remove the empty array on line 18 (so
  // there is no dependency list, what happens?)
  // console.log({ cards });

  for (const currentCard of cards) {
    tradingCards.push(
      <TradingCard
        key={currentCard.name}
        name={currentCard.name}
        skill={currentCard.skill}
        imgUrl={currentCard.imgUrl}
      />
    );
  }

  return <div>{tradingCards}</div>;
}


ReactDOM.render(
  <TradingCardContainer />,
  document.getElementById('container')
);
