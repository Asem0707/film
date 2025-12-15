import FilmCard from '../../components/FilmCard'


export default async function Films(){
const res = await fetch('http://localhost:8000/films/')
const movies = await res.json()



return (
<div>
<h2 className="text-2xl font-bold mb-4">Каталог фильмов</h2>
<div className="grid grid-cols-2 md:grid-cols-4 gap-4">
{movies.map(m => <FilmCard key={m.id} movie={m} />)}
</div>
</div>
)
}
