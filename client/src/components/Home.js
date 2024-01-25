import { useEffect, useState } from "react";
import { Link} from "react-router-dom";

function Home() {
  const [restaurants, setRestaurants] = useState([]);

 
  useEffect(() => {
    fetch("/restaurants")
      .then((r) => r.json())
      .then(setRestaurants);
  }, []);

   function handleDelete(id) {
    fetch(`/restaurants/${id}`, {
      method: "DELETE",
    }).then((r) => {
      if (r.ok) {
        setRestaurants((restaurants) =>
          restaurants.filter((restaurant) => restaurant.id !== id)
        );
      }
    });
  }


  return (
    <section>
      <h2>All Restaurants</h2>
      <ul>
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            <Link to={`/restaurants/${restaurant.id}`}>{restaurant.name}</Link>
            <button onClick={()=>handleDelete(restaurant.id)}>delete Restaurant</button>
          </li>
        ))}
      </ul>
    </section>
  );
}

export default Home;