import { Link, useMatch, useResolvedPath } from 'react-router-dom';
import './Navbar.css';
export default function Navbar(){
  return (
    <nav className="nav">
      <a href="/" className="site-title">JolsAid</a>
      <ul>
        <CustomLink href="/deals">Deals</CustomLink>
        <CustomLink href="/products">Products</CustomLink>
        <CustomLink href="/brands">Brands</CustomLink>
      </ul>
    </nav>
  )
}
function CustomLink({ href, children, ...props}) {
  const path = window.location.pathname
  return (
    <li className= {path === href ? "active" : ""}>
      <a href={href} {...props}>
        {children}
      </a>
    </li>
  )}
// {/* //     return (
// //         <nav className="nav">
// //             <Link to = "/" className="site-title">JolsAid</Link>
// //             <ul>
// //                 <CustomLink to = "/deals">Deals</CustomLink>
// //                 <CustomLink to = "/products">Products</CustomLink>
// //             </ul>
// //         </nav>
// //     );
// // } */}

// // function CustomLink({ to, children, ...props }) {
// //     const resolvedPath = useResolvedPath(to)
// //     const isActive = useMatch({ path: resolvedPath.pathname, end: true })
  
// //     return (
// //       <li className={isActive ? "active" : ""}>
// //         <Link to={to} {...props}>
// //           {children}
// //         </Link>
// //       </li>
// //     )
// //   }