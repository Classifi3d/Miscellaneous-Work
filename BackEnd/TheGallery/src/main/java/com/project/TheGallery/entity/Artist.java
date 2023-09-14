package com.project.TheGallery.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "gallerytable")
public class Artist {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id", nullable = false)

    private Integer id;
    @Column(name = "name", nullable = false)
    private String name;
    @Column(name = "years", nullable = false)
    private String years;
    @Column(name = "genre", nullable = false)
    private String genre;
    @Column(name = "nationality", nullable = false)
    private String nationality;
    @Column(name = "bio", nullable = false)
    private String bio;
    @Column(name = "wikipedia", nullable = false)
    private String wikipedia;
    @Column(name = "paintings", nullable = false)
    private Integer paintings;


    public Artist(Integer id, String name, String years, String genre, String nationality, String bio, String wikipedia, Integer paintings) {
        this.id = id;
        this.name = name;
        this.years = years;
        this.genre = genre;
        this.nationality = nationality;
        this.bio = bio;
        this.wikipedia = wikipedia;
        this.paintings = paintings;
    }

    public Artist() {
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getYears() {
        return years;
    }

    public void setYears(String years) {
        this.years = years;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public String getNationality() {
        return nationality;
    }

    public void setNationality(String nationality) {
        this.nationality = nationality;
    }

    public String getBio() {
        return bio;
    }

    public void setBio(String bio) {
        this.bio = bio;
    }

    public String getWikipedia() {
        return wikipedia;
    }

    public void setWikipedia(String wikipedia) {
        this.wikipedia = wikipedia;
    }

    public Integer getPaintings() {
        return paintings;
    }

    public void setPaintings(Integer paintings) {
        this.paintings = paintings;
    }

    @Override
    public String toString() {
        return "Artist{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", years='" + years + '\'' +
                ", genre='" + genre + '\'' +
                ", nationality='" + nationality + '\'' +
                ", bio='" + bio + '\'' +
                ", wikipedia='" + wikipedia + '\'' +
                ", paintings=" + paintings +
                '}';
    }
}
