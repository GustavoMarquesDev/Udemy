const express = require("express");
const router = express.Router();
const Job = require("../models/Job");
const Sequelize = require("sequelize");
const Op = Sequelize.Op;

router.get("/", (req, res) => {
  let search = req.query.job;
  let query = "%" + search + "%"; // para fazer as pesquisar aproximadas como Ph ser php e por ai vai

  if (!search) {
    Job.findAll({ order: [["createdAt", "DESC"]] })
      .then((jobs) => {
        res.render("index", {
          jobs,
        });
      })
      .catch((err) => console.log(err));
  } else {
    Job.findAll({
      where: { title: { [Op.like]: query } },
      order: [["createdAt", "DESC"]],
    })
      .then((jobs) => {
        res.render("index", {
          jobs,
          search,
        });
      })
      .catch((err) => console.log(err));
  }
});

router.get("/test", (req, res) => {
  res.send("deu certo index");
});

module.exports = router;
