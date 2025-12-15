import FilmCard from '../../../components/FilmCard'


export default async function FilmPage({ params }){
const id = params.id
const res = await fetch(`http://localhost:8000/movies/${id}`)
if (!res.ok) return <div>Фильм не найден</div>
const movie = await res.json()


return (
<div className="max-w-3xl">
<img src={movie.poster} alt={movie.title} className="w-full h-96 object-cover rounded" />
<h1 className="text-3xl font-bold mt-4">{movie.title}</h1>
<p className="text-gray-400">{movie.year}</p>
<p className="mt-4">{movie.description}</p>
</div>
)
}