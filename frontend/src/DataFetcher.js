import React, { useState, useEffect } from 'react'
import axios from 'axios'

function DataFetcher() {
   const [data, setData] = useState(null)

   useEffect(() => {
      const fetchData = async () => {
         try {
            const response = await axios.get('http://127.0.0.1:5000/data')
            setData(response.data)
         } catch (error) {
            console.error('Error fetching data:', error)
         }
      }

      fetchData();
   }, [])

   // Log the data to see its structure
   console.log("Data:", data);

   return (
      <div>
         <h1>Scraped data</h1>
         {data ? ( // Ensure data is not null before accessing its properties
            <div>
               <h2>Products</h2>
               <ul>
                  {data.products.map((product, index) => (
                     <li key={index}>
                        <strong>{product}</strong>
                        <ul>
                           <li>Old Price: {data.oldprices[index]}</li>
                           <li>New Price: {data.newprices[index]}</li>
                           <li>Link: <a href={data.links[index]}>{data.links[index]}</a></li>
                           <li>Stock: {data.stock[index] === 1 ? 'Available' : 'Out of Stock'}</li>
                        </ul>
                     </li>
                  ))}
               </ul>
            </div>
         ) : (
            <p>Loading...</p> // Display a loading message while data is being fetched
         )}
      </div>
   )
}

export default DataFetcher;
