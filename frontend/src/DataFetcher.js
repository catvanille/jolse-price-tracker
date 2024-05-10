import React, { useState, useEffect } from 'react'
import axios from 'axios'

function DataFetcher() {
   const [data, setData] = useState(null)

   useEffect(() => {
      const fetchData = async () => {
         try {
            const response = await axios.get('http://localhost:3000/data')
            setData(response.data)
         } catch (error) {
            console.error('Error fetching data:', error)
         }
      }

      fetchData();
   }, [])

   return (
      <div>
         <h1>Scraped data</h1>
         {data && (
            <div>
               <h2>Products</h2>
               <ul>
                  {data.products.map((product, index) => (
                     <li key={index}>{product}</li>
                  ))}
               </ul>
            </div>
         )}
      </div>
   )
}

export default DataFetcher;