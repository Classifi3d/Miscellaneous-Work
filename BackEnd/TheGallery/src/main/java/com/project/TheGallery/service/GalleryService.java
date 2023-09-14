package com.project.TheGallery.service;

import com.project.TheGallery.entity.Artist;

import java.util.List;

public interface GalleryService {

    public List<Artist> fetchArtistList();

    public Artist fetchArtistId(Integer artistId);

    public Artist fetchArtistRandom();
    public List<Artist> fetchArtistRandomList(Integer artistCount);
    public List<Artist> fetchArtistRandom10();

    public Artist fetchArtistByName(String artistName);

//    public Artist fetchArtistPicureById(String artistName,Integer pictureId);

}
