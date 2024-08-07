// Cria um usuário admin com privilégios completos
db.createUser({
  user: "davidade",
  pwd: "aderaldo01",
  roles: [{ role: "root", db: "admin" }],
});
