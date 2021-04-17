from flask import Flask, render_template, jsonify, request
from model import db, connect_to_db, Card
app = Flask(__name__)

@app.route("/")
def show_homepage():
    """Show the application's homepage."""

    return render_template("homepage.html")

@app.route("/cards")
def show_cards():
    """Show all trading cards."""

    return render_template("cards.html")

@app.route("/cards.json")
def get_cards_json():
    """Return a JSON response with all cards in DB."""

    cards = Card.query.all()
    cards_list = []

    for c in cards:
        cards_list.append({"skill": c.skill, "name": c.name, "imgUrl": c.image_url, "cardId": c.card_id})

    return {"cards": cards_list}

@app.route("/add-card", methods=["POST"])
def add_card():
    """Add a new card to the DB."""
    name = request.get_json().get('name')
    skill = request.get_json().get('skill')

    new_card = Card(name=name, skill=skill)
    db.session.add(new_card)
    db.session.commit()
    # the new_card variable we created on line 35 did not have its card_id set
    # we call db.session.refresh(new_card) to update the variable to the version from the database
    # that way, its card_id will be set
    db.session.refresh(new_card)
    return {"success": True, "cardAdded": {"skill": new_card.skill, "name": new_card.name, "imgUrl": new_card.image_url, "cardId": new_card.card_id}}

@app.route("/cards-jquery")
def show_cards_jquery():
    return render_template("cards-jquery.html")

if __name__ == "__main__":
  connect_to_db(app)
  app.run(debug=True, host='0.0.0.0')
