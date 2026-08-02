import axios from "axios";
import { useEffect, useState } from "react";
function Category() {
  interface Category {
    id: number;
    name: string;
  }
  const [category, setCategory] = useState<Category[]>([]);
  useEffect(() => {
    axios
      .get("http://localhost:8000/api/v1/category/")
      .then((res) => {
        setCategory(res.data);
      })
      .catch((err) => console.log(err));
  }, []);
  return (
    <>
      <h2 className="text-4xl text-orange-500 text-center">Category</h2>
      {category.map((item, index) => (
        <div
          key={index}
          className="h-30 flex relative justify-center items-center w-70 bg-amber-200 mt-3"
        >
          <ul className="list-none m-0 p-0">
            <li className="absolute left-1 top-1">{item.id}</li>
            <li>{item.name}</li>
          </ul>
        </div>
      ))}
    </>
  );
}

export default Category;
